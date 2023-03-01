import React, { useState, useEffect } from 'react'
import axios from 'axios';
import { useParams } from 'react-router-dom';
import styles from './Company.module.scss'
import DataField from './../../components/data_field/DataField';
import SocialShare from './../../components/social_shares/SocialShare';

const Company = () => {
   const {slug} = useParams();
   const [company, setCompany] = useState([]);
   const [error, setError] = useState("");
   const [socialMedias, setSocialMedias] = useState([])

   useEffect(() => {
      getCompany();
      document.title = 'Company';
   }, [])

   const getCompany = async () => {
      // U NEED TO CHANGE 
      axios.get(`http://127.0.0.1:8000/api/${slug}`)
         .then(res => {
               console.log(res.data)
               setCompany(res.data)
               setSocialMedias(res.data.social_medias)
            }
         )
   }

   const handleContactClick = () => {
      try {
         const options = { name: company.username };
         const contact = new window.navigator.contacts.Contact(options);
         const phoneNumbers = [new window.navigator.contacts.ContactField('mobile', company.number)];
         contact.phoneNumbers = phoneNumbers;
         contact.save(() => alert('Contact saved!'));
      }catch(err) {
         console.error(err);
         window.location.href = `tel:${company.number}`;
      }
    }


   return (
      <>
         <div className={styles.card}>
            <div className={styles.card__item}>
               <div className={styles.data__image}>
                  <img src={`http://127.0.0.1:8000/static/media/${company.ava}`} alt={company.ava}/>
                  <h2>{company.username}</h2>
               </div>
               {company.location? <DataField title={`Место:  `} data={company.email}/> : "" }
               {company.title? <DataField title={`Заголовок: `} data={company.title}/> : "" }
               {company.email? <DataField title={`Почта: `} data={company.email}/> : "" }
               {company.number? <DataField title={`Номер: `} data={company.number}/> : "" }

               <button className={styles.btn} onClick={handleContactClick}>Сохранить</button>

               <SocialShare social={socialMedias} />
            </div>
      </div>
      </>
   )
}

export default Company