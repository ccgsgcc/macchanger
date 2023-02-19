import React from 'react';
import styles from './Message.module.scss'

const Message = ({bottom}) => {
  return (
    <div className={styles.message} style={{bottom: bottom}}>Скопировано!</div>
  )
}

export default Message