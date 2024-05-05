const showBtn = document.querySelectorAll(".showBtn");
const cancelBtn = document.querySelectorAll(".cancel-btn");

showBtn.forEach((elem) => {
  elem.addEventListener("click", (e) => {
    e.preventDefault()
    let elemParent = elem.parentElement.parentElement;
    candidateDetail = elemParent.querySelector(".candidate-detail");
    candidateDetail.classList.toggle("hide")
  })
})

cancelBtn.forEach((elem) => {
  elem.addEventListener("click", (e) => {
    e.preventDefault()
    let elemParent = elem.parentElement;
    candidateDetail.classList.toggle("hide");
  })
})