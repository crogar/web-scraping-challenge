function wind_load()
{
    var heights = window.innerWidth;
    document.getElementsByClassName("stars")[0].style.height = (heights*0.75) + "px";
    document.getElementsByClassName("twinkling")[0].style.height = (heights*0.75) + "px";
    console.log(heights);
}


function reportWindowSize() {
    var heights = window.innerWidth;
    document.getElementsByClassName("stars")[0].style.height = (heights*1.2) + "px";
    document.getElementsByClassName("twinkling")[0].style.height = (heights*1.2) + "px";
    console.log("resized");
  }
  
  window.onload = function() {
    wind_load();
};

  // window.addEventListener('resize', reportWindowSize);