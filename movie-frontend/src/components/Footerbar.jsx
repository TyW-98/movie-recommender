import twitterIcon from "../assets/icons8-twitter.svg";
import youtubeIcon from "../assets/icons8-youtube.svg";
import githubIcon from "../assets/icons8-github.svg";

export default function Footebar() {
  return (
    <div className="footer-container">
      <div className="footer-socialicons">
        <img src={twitterIcon} className="social-icons" alt="twitter icon" />
        <img src={youtubeIcon} className="social-icons" alt="youtube icon" />
        <img src={githubIcon} className="social-icons" alt="github icon" />
      </div>
      <h5>© TyW-98. All rights reserved.</h5>
    </div>
  );
}
