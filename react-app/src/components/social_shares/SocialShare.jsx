import React from 'react';
import styles from './SocialShare.module.scss';

/*  __ICONS__*/
import {
   BsFacebook, 
   BsInstagram, 
   BsDiscord,
   BsGithub,
   BsLinkedin,
   BsPinterest,
   // FaSkype,
   FaSnapchatGhost,
   FaSoundcloud,
   FaSpotify,
   FaTelegram,
   FaTiktok,
   FaTwitch,
   FaTwitter,
   FaViber,
   FaVk,
   FaWhatsapp,
   FaYoutube
} from 'react-icons/bs'
import {FaQuora} from 'react-icons/fa';
import {SiSinaweibo, SiSkype, SiTiktok, SiViber, SiVk} from 'react-icons/si';
import {TiSocialTumblerCircular} from 'react-icons/ti';
import {
   BsSnapchat,
    BsSpotify, 
    BsTelegram, 
    BsTwitch,
    BsTwitter,
    BsWhatsapp
} from 'react-icons/bs';
import {GrSoundcloud} from 'react-icons/gr'
import {AiFillYoutube} from 'react-icons/ai';

function SocialShare({social}) {

   return (
   <div className={styles.data__icons}>
         {social.facebook? <a href={social.facebook}><BsFacebook className= {styles.icon} /></a> : '' }
         {social.instagram? <a href={social.instagram}><BsInstagram className= {styles.icon} /></a> : '' }
         {social.discord? <a href={social.discord}><BsDiscord className= {styles.icon} /></a> : '' }
         {social.github? <a href={social.github}><BsGithub className= {styles.icon} /></a> : '' }
         {social.linkedin? <a href={social.linkedin}><BsLinkedin className= {styles.icon} /></a> : '' }
         {social.pinterest? <a href={social.pinterest}><BsPinterest className= {styles.icon} /></a> : '' }
         {social.quora? <a href={social.quora}><FaQuora className= {styles.icon} /></a> : '' }
         {social.sinaweibo ? <a href={social.sinaweibo}><SiSinaweibo className= {styles.icon} /></a> : '' }
         {social.skype ? <a href={social.skype}><SiSkype className= {styles.icon} /></a> : '' }
         {social.snapChat ? <a href={social.snapChat}><BsSnapchat className= {styles.icon} /></a> : '' }
         {social.soundCloud ? <a href={social.soundCloud}><GrSoundcloud className= {styles.icon} /></a> : '' }
         {social.spotify ? <a href={social.spotify}><BsSpotify className= {styles.icon} /></a> : '' }
         {social.telegram ? <a href={social.telegram}><BsTelegram className= {styles.icon} /></a> : '' }
         {social.tiktok ? <a href={social.tiktok}><SiTiktok className= {styles.icon} /></a> : '' }
         {social.tumbler ? <a href={social.tumbler}><TiSocialTumblerCircular className= {styles.icon} /></a> : '' }
         {social.twitch ? <a href={social.twitch}><BsTwitch className= {styles.icon} /></a> : '' }
         {social.twitter ? <a href={social.twitter}><BsTwitter className= {styles.icon} /></a> : '' }
         {social.viber ? <a href={social.viber}><SiViber className= {styles.icon} /></a> : '' }
         {social.vk ? <a href={social.vk}><SiVk className= {styles.icon} /></a> : '' }
         {social.whatsapp ? <a href={social.whatsapp}><BsWhatsapp className= {styles.icon} /></a> : '' }
         {social.youtube ? <a href={social.youtube}><AiFillYoutube className= {styles.icon} /></a> : '' }

   </div>
   )
}

export default SocialShare