const display = document.querySelector('.display');
const btnNumber = document.querySelectorAll('.numbers');



display.textContent = '';

btnNumber.forEach(button => {
    button.addEventListener('click', () => {
        display.textContent += button.textContent
    })
})

const deleteNumber = () => {
    display.textContent = display.textContent.slice(1, -1)
}


document.querySelector('.apagar')
    .addEventListener('click', deleteNumber);