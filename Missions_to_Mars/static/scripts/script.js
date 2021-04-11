function resize()
{
    var heights = window.innerWidth;
    document.getElementsByClassName("stars")[0].style.height = (heights) + "px";
    document.getElementsByClassName("twinkling")[0].style.height = (heights) + "px";
    console.log(heights);
}

window.onload = function() {
    resize();
};