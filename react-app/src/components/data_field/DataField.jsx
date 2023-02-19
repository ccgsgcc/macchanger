import React, {useState} from 'react';
import styles from './DataFiels.module.scss'
import Message from './../ui/message/Message';

const DataField = ({title, data}) => {
  const [bottom, setBottom] = useState('-10%');
  
  const copy = () => {
    setBottom('10%')
    navigator.clipboard.writeText(data)

    setTimeout(() => {
      setBottom('-10%')
    }, 1500)
  }

  return (
    <>
      <div className={styles.data__field}>
        <label>{title} </label>
        <p  className={styles.text}  onClick={copy}> {data}</p>
      </div>
      <Message bottom={bottom} />
    </>
  )
}

export default DataField