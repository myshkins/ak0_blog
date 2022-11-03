const likeButton = document.querySelector('.heart-wrap')
const likeCount = document.querySelector('.like-count span')
const heartImg = document.querySelector('.hearted')
const isItLiked = document.querySelector('.is-it-liked')

likeButton.addEventListener('click', addLike)

const updateHeart = () => {
    console.log('heart update')
    if (isItLiked.textContent === 'liked') {
        console.log('hearted')
        heartImg.src = "/static/img/heart-fill.png"
        likeButton.removeEventListener('click', addLike)
    } else {
        console.log('not hearted')
        heartImg.src = "/static/img/heart-outline.png"
    }
}

heartUpdater = updateHeart
heartUpdater()

const updateLikes = (jsonData) => {
    console.log(jsonData)
    likeCount.textContent = jsonData['likes'] + " " + "likes"
}

function addLike(e) {
    console.log(e)
    window.location.reload()
    fetch('/like')
        .then((response) => response.json())
        .then(updateLikes)
    likeButton.removeEventListener('click', addLike)
    updateHeart()

}