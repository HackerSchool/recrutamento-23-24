use core::fmt;

#[derive(Clone, Debug, PartialEq)]
pub struct Task {
    title: String,
    description: String,
}

impl Task {
    fn new(title: String, description: String) -> Task {
        Task { title, description }
    }
}

impl fmt::Display for Task {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}: {}", self.title, self.description)
    }
}

pub struct TaskManager {
    tasks: Vec<Task>,
}

impl TaskManager {
    pub fn new() -> TaskManager {
        TaskManager { tasks: Vec::new() }
    }

    pub fn create_task(&mut self, title: &str, description: &str) -> &Task {
        let task = Task::new(title.to_string(), description.to_string());

        self.tasks.push(task);

        &self.tasks[self.tasks.len() - 1]
    }

    pub fn list(&self) -> impl Iterator<Item = &Task> {
        self.tasks.iter()
    }

    pub fn edit(
        &mut self,
        title: &str,
        new_title: Option<&str>,
        new_description: Option<&str>,
    ) -> Option<&Task> {
        if let Some(position) = self.tasks.iter().position(|task| task.title == title) {
            if let Some(task) = self.tasks.get_mut(position) {
                if let Some(new_title) = new_title {
                    task.title = new_title.to_string();
                }
                if let Some(new_description) = new_description {
                    task.description = new_description.to_string();
                }

                Some(task)
            } else {
                unreachable!("The position should be valid.")
            }
        } else {
            None
        }
    }

    pub fn delete(&mut self, title: &str) -> Option<Task> {
        if let Some(position) = self.tasks.iter().position(|task| task.title == *title) {
            Some(self.tasks.remove(position))
        } else {
            None
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn create_and_list_tasks() {
        let mut manager = TaskManager::new();

        let task1 = manager.create_task("Task 1", "Description 1").clone();
        let task2 = manager.create_task("Task 2", "Description 2").clone();

        let tasks: Vec<_> = manager.list().collect();
        assert_eq!(tasks, vec![&task1, &task2]);
    }

    #[test]
    fn edit_task() {
        let mut manager = TaskManager::new();
        manager.create_task("Original Title", "Original Description");

        let task = manager
            .edit("Original Title", Some("New Title"), Some("New Description"))
            .unwrap();

        assert_eq!(task.title, "New Title");
        assert_eq!(task.description, "New Description");
    }

    #[test]
    fn edit_nonexistent_task() {
        let mut manager = TaskManager::new();
        manager.create_task("Task 1", "Description 1");

        let result = manager.edit(
            "Nonexistent Task",
            Some("New Title"),
            Some("New Description"),
        );

        assert_eq!(result, None);
    }

    #[test]
    fn delete_task() {
        let mut manager = TaskManager::new();
        let task = manager.create_task("Task to Delete", "Description").clone();

        let deleted_task = manager.delete("Task to Delete").unwrap();

        assert_eq!(deleted_task, task);
    }

    #[test]
    fn delete_nonexistent_task() {
        let mut manager = TaskManager::new();
        manager.create_task("Task 1", "Description 1");

        let result = manager.delete("Nonexistent Task");

        assert_eq!(result, None);
    }
}
