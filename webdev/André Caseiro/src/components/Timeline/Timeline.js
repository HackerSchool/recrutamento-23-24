import './Timeline.css';
import timeline from "../../data/timeline.json";

function TimelineItem({ title, institution, link, description, icon, from, to }) {

  let institutionDiv = null;
  if (institution) {
    institutionDiv = (
      <p className="institution">
        {"at " + institution}
        <a href={link} target="_blank" rel="noopener noreferrer">
          &#x2197;
        </a>
      </p>
    )
  }

  return (
    <div className="timelineItem">
      <div className="dates">
        <p className='duration'>{from + " - " + (to || "PRESENT")}</p>
        <div className="image">
          <img src={icon} alt={title} />
        </div>
      </div>
      <div className="info">
        <h3>{title}</h3>
        {institutionDiv}
        {description ? (<p>{description}</p>) : <></>}
      </div>
    </div >
  );
}

function Timeline() {
  return (
    <>
      <h2 className="timelineTitle">Timeline</h2>
      <div className="timeline">
        {timeline.list.map(e => <TimelineItem {...e} />)}
      </div>
    </>
  );
}

export default Timeline;
