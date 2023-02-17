
const texts = document.querySelectorAll('.text')
const message = document.querySelector('.message')

//When U click on a text
for (let text of texts) {
   text.onclick = () => {
      copy(text.innerHTML)
      message.style.bottom = '10%'
      console.log(text.innerHTML);

      setTimeout(() => {
         message.style.bottom = '-10%'
      }, 1000)
   }
}

//? Copy function
function copy(offer) {
   navigator.clipboard.writeText(offer)
}
