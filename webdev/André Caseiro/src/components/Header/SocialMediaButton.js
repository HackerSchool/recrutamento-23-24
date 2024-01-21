import React from 'react';
import PropTypes from 'prop-types';
import './SocialMediaButton.css';

const SocialMediaButton = ({ title, icon, link }) => {
  return (
    <a href={link} className="social-media-button" target="_blank" rel="noopener noreferrer">
      <div className="social-media-icon">
        <img src={icon} alt={title + " link"} />
      </div>
    </a>
  );
};

SocialMediaButton.propTypes = {
  title: PropTypes.string.isRequired,
  icon: PropTypes.string.isRequired,
  link: PropTypes.string.isRequired,
};

export default SocialMediaButton;
