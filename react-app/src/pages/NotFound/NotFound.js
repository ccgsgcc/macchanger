import React from 'react';
import {BiPlanet} from 'react-icons/bi';
import styles from './NotFound.module.scss';

const NotFound = () => {
  return (
    <div className = {styles.NotFound}>
      <h1>Not Found</h1>
      <BiPlanet className={styles.icon} />
    </div>
  )
}

export default NotFound