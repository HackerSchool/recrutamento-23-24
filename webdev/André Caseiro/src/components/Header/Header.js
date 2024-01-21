import './Header.css';
import header from "../../data/header.json";
import SocialMediaButton from './SocialMediaButton';

import { ExpandMore } from '@mui/icons-material';

function Header() {
  function handleScroll() {
    window.scrollBy({
      top: 100,
      behavior: 'smooth',
    });
  };

  return (
    <header className='mainHeader'>
      <div>
        <div className='info'>
          <p>Hello, I'm</p>
          <h1>{header.name}</h1>
          <div className='socialMedia'>
            {
              header.socialMedia.map(e => (
                <SocialMediaButton
                  title={e.title}
                  icon={e.icon}
                  link={e.link}
                />
              ))
            }
          </div>
        </div>
        <div className='picture'>
          <img src={header.picture} alt={header.name + " profile picture"} />
        </div>
      </div>
      <div className='scroll-indicator' onClick={handleScroll}>
        <ExpandMore />
      </div>
    </header>
  );
}

export default Header;
