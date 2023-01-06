let bigImage = document.getElementById("big-image")
let smallImage = document.getElementsByClassName("small-image")

//    console.log(bigImage)
//    console.log(smallImage)
for(let i = 0;i<smallImage.length;i++) {
     smallImage[i].addEventListener("click",function(){
         let src = smallImage[i].getAttribute("src")
         bigImage.setAttribute("src",src)
     })
}