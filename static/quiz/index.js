let quiz = document.getElementById('quiz_activate')
let quiz_deactivate = document.getElementById('quiz_deactivate')
let quiz_block = document.querySelector('.quiz')
quiz.addEventListener('click', ()=>{
    quiz_block.classList.toggle('quiz-active')
    quiz_deactivate.classList.toggle('quiz_activate12')
})

let elements = document.querySelectorAll('.quiz__block');
let currentIndex = 0;
let showPreviousButton = document.querySelector('#prev_q');
let showNextButton = document.querySelector('#next_q');
let submitButton = document.querySelector('#submit_q');
const inputResult = document.getElementById('fullinfo')
const quiz__error = document.querySelector('.quiz__error')
const ok_btn = document.querySelector('#ok_btn')

quiz_deactivate.addEventListener('click', ()=>{
    quiz_block.classList.remove('quiz-active')
    quiz_deactivate.classList.remove('quiz_activate12')

})

function showPrevious() {
    elements[currentIndex].classList.remove('visible2');
    currentIndex = (currentIndex - 1 + elements.length) % elements.length;
    elements[currentIndex].classList.add('visible2');
    updateButtonVisibility();
    quiz__error.style.display = 'none'
}

function showNext() {
    if (validateInputs(currentIndex+1)) {
        elements[currentIndex].classList.remove('visible2');
        currentIndex = (currentIndex + 1) % elements.length;
        elements[currentIndex].classList.add('visible2');
        updateButtonVisibility();
        quiz__error.style.display = 'none'
    }
}

function check_inputs() {
    const name = document.querySelector('[id="name"]')
    const phone = document.querySelector('[id="phone"]')
    return name.value != '' && phone.value != '' ? true : false
}

function validateInputs(id){
    let radio_btns = document.querySelectorAll(`input[id="radio_btn radio_btn${id}"]:checked`)
    if (id == 3) {
        let inpname = document.querySelector('#radio_btn3')
        inputResult.value += `${id}:${inpname.value}\n`
        return true
    }
    if (radio_btns.length !=0) {
        let quiz = ''
        radio_btns.forEach((e)=>{
            quiz += `${e.value}, `
        })
        inputResult.value += `${id}:${quiz}\n`
        return true
    }
    else{
        quiz__error.style.display = 'flex'
        return false
    }
}

function updateButtonVisibility() {
    showPreviousButton.style.display = currentIndex === 0 ? 'none' : 'block';
    showNextButton.style.display = currentIndex === elements.length - 1 ? 'none' : 'block';
    submitButton.style.display = currentIndex === elements.length - 1 ? 'block' : 'none';
}

elements[currentIndex].classList.add('visible2');
updateButtonVisibility();

ok_btn.addEventListener('click', ()=>{
    quiz__error.style.display = 'none'
})

let radio_btns = document.querySelectorAll('input[type=checkbox]')
let quiz__div = document.querySelector('.quiz__div')
radio_btns.forEach((e)=>{
    e.addEventListener('click', ()=>{
        e.parentElement.lastElementChild.classList.toggle('label-active')
    })
})
