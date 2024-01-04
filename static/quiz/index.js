let quiz = document.getElementById('quiz_activate')
let quiz_block = document.querySelector('.quiz')
quiz.addEventListener('click', ()=>{
    quiz_block.classList.toggle('quiz-active')
})

let elements = document.querySelectorAll('.quiz__block');
let currentIndex = 0;
let showPreviousButton = document.querySelector('#prev_q');
let showNextButton = document.querySelector('#next_q');
let submitButton = document.querySelector('#submit_q');
const inputResult = document.getElementById('quiz_result')
const quiz__error = document.querySelector('.quiz__error')
const ok_btn = document.querySelector('#ok_btn')

function showPrevious() {
    elements[currentIndex].classList.remove('visible');
    currentIndex = (currentIndex - 1 + elements.length) % elements.length;
    elements[currentIndex].classList.add('visible');
    updateButtonVisibility();
}

function showNext() {
    if (validateInputs(currentIndex+1)) {
        elements[currentIndex].classList.remove('visible');
        currentIndex = (currentIndex + 1) % elements.length;
        elements[currentIndex].classList.add('visible');
        updateButtonVisibility();
    }
}
ok_btn.addEventListener('click', ()=>{
    quiz__error.style.display = 'none'
})
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
    console.log(inputResult.value);
}

elements[currentIndex].classList.add('visible');
updateButtonVisibility();


let radio_btns = document.querySelectorAll('input[type=checkbox]')
let quiz__div = document.querySelector('.quiz__div')
radio_btns.forEach((e)=>{
    e.addEventListener('click', ()=>{
        e.parentElement.lastElementChild.classList.toggle('label-active')
    })
})

