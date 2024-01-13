use std::io::{self, Write};

use clap::{command, Arg, ArgMatches, Command};
use task_manager::TaskManager;

fn main() {
    // Create the task manager
    let mut task_manager = TaskManager::new();

    // Create the command parser
    let mut cmd = cmd();

    // Print initial message
    print!("{}", cmd.render_long_help());

    loop {
        let input = prompt();

        let matches = match cmd.try_get_matches_from_mut(split_input(&input)) {
            Ok(matches) => matches,
            Err(e) => {
                print!("{e}");
                continue;
            }
        };

        match matches.subcommand() {
            Some(("new", sub_matches)) => new(&mut task_manager, sub_matches),
            Some(("list", _)) => list(&mut task_manager),
            Some(("edit", sub_matches)) => edit(&mut task_manager, sub_matches),
            Some(("delete", sub_matches)) => delete(&mut task_manager, sub_matches),
            Some(("exit", _)) => break,
            Some(("help", sub_matches)) => help(&mut cmd, sub_matches),

            _ => unreachable!(
                "Exhausted list of subcommands and subcommand_required prevents `None`"
            ),
        }
    }
}

/// Prompt the user for input and return the entered line.
fn prompt() -> String {
    print!("> ");
    io::stdout().flush().expect("Failed to flush stdout");
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    input
}

// Tokenize the input, spliting on whitespaces outside quotes
fn split_input(input: &str) -> Vec<String> {
    let mut result = Vec::new();
    let mut current_word = String::new();
    let mut in_quotes = false;

    for c in input.chars() {
        match c {
            c if c.is_whitespace() && !in_quotes => {
                if !current_word.is_empty() {
                    result.push(current_word.clone());
                    current_word.clear();
                }
            }
            '"' => {
                in_quotes = !in_quotes;
            }
            _ => {
                current_word.push(c);
            }
        }
    }

    if !current_word.is_empty() {
        result.push(current_word);
    }

    result
}

// Build the CLI
fn cmd() -> Command {
    command!()
        .name("")
        .no_binary_name(true)
        .disable_help_flag(true)
        .disable_version_flag(true)
        .disable_help_subcommand(true)
        .subcommand(
            Command::new("new")
                .arg(Arg::new("title").required(true).help("Task title"))
                .arg(
                    Arg::new("description")
                        .default_value("")
                        .help("Task description"),
                )
                .about("Create a new task."),
        )
        .subcommand(Command::new("list").about("List all tasks."))
        .subcommand(
            Command::new("edit")
                .arg(
                    Arg::new("old_title")
                        .required(true)
                        .help("Title of the task to edit"),
                )
                .arg(Arg::new("new_title").required(false).help("New task title"))
                .arg(
                    Arg::new("new_description")
                        .required(false)
                        .help("New task description"),
                )
                .about("Edit a task title or description."),
        )
        .subcommand(
            Command::new("delete")
                .arg(
                    Arg::new("title")
                        .required(true)
                        .help("Title of the task to delete"),
                )
                .about("Delete a task by name."),
        )
        .subcommand(Command::new("exit").about("Exit the app."))
        .subcommand(
            Command::new("help")
                .arg(Arg::new("cmd").required(false).help("Command to get usage"))
                .about("Print usage of a command."),
        )
        .after_long_help("Tip: use quotes to enter fields containing whitespaces.")
}

fn new(task_manager: &mut TaskManager, sub_matches: &ArgMatches) {
    let _ = task_manager.create_task(
        sub_matches.get_one::<String>("title").unwrap(),
        sub_matches.get_one::<String>("description").unwrap(),
    );
}

fn list(task_manager: &mut TaskManager) {
    let mut count = 0;

    task_manager.list().enumerate().for_each(|(i, task)| {
        count += 1;
        println!("{i}. {task}");
    });

    if count == 0 {
        println!("There are no tasks to list.");
    }
}

fn edit(task_manager: &mut TaskManager, sub_matches: &ArgMatches) {
    if let None = task_manager.edit(
        sub_matches.get_one::<String>("old_title").unwrap(),
        sub_matches
            .get_one::<String>("new_title")
            .map(|x| x.as_str()),
        sub_matches
            .get_one::<String>("new_description")
            .map(|x| x.as_str()),
    ) {
        println!("Failed to edit task.");
    }
}

fn delete(task_manager: &mut TaskManager, sub_matches: &ArgMatches) {
    if let None = task_manager.delete(sub_matches.get_one::<String>("title").unwrap()) {
        println!("Failed to delete task.");
    }
}

fn help(cmd: &mut Command, sub_matches: &ArgMatches) {
    if let Some(subcommand_name) = sub_matches.get_one::<String>("cmd") {
        let mut valid_command = true;

        if let Some(subcommand) = cmd
            .get_subcommands_mut()
            .find(|subcommand| subcommand.get_name() == subcommand_name)
        {
            print!("{}", subcommand.render_help());
        } else {
            valid_command = false;
        }

        if !valid_command {
            print!("{}", cmd.render_help());
        }
    } else {
        print!("{}", cmd.render_help());
    }
}
