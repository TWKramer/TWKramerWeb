var dt = new Date();
                document.getElementById("datetime").innerHTML = dt.toLocaleDateString();

$(".card").click(function(){
    window.location=$(this).find("card-content3").attr("href"); 
    return false;
    });






