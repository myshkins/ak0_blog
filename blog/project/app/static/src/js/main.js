const likeButton = document.querySelector('.heart-wrap')
const likeCount = document.querySelector('.like-count span')
const heartedImg = document.getElementById('heart-fill')
const notHeartedImg = document.querySelector('.not-hearted')
// const isItLiked = document.querySelector('.is-it-liked')

likeButton.addEventListener('click', addLike)

const updateHeart = () => {
    if (document.querySelector('.is-it-liked')) {
        heartedImg.classList.remove('unhearted')
        heartedImg.classList.add('hearted')
        likeButton.removeEventListener('click', addLike)
    } else {
        heartedImg.classList.add('unhearted')
    }
}

heartUpdater = updateHeart
heartUpdater()

const updateLikes = () => {
    newCount = likeCount.textContent.split(' ')[0] + 1
    likeCount.textContent = newCount + " " + "likes"
    heartUpdater()
}


function addLike(e) {
    window.location.reload()
    fetch('/like')
        // .then((response) => response.json())
        // .then(updateLikes)
    likeButton.removeEventListener('click', addLike)
    heartedImg.classList.add('hearted')
    updateHeart()
    location.reload()
}