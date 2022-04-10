<script>

$( document ).ready(function() {
   checkCookie()
});

$('#darkmode').click(function(){
  var text = $('.darkmode-text').text()
  if (text ==="Darkmode aktivieren"){
    darkmode("black")
  }
  else{
    darkmode("white")
  }
});

  function checkCookie()
  {
    var checkcookie= document.cookie.indexOf('darkmode');
    if (checkcookie != -1){
      darkmode("black")
    }
   else {
      darkmode("white")
   }
  }

  function darkmode(color){

    if (color ==="black"){
    document.cookie = "darkmode=true; expires=Fri, 31 Dec 9999 23:59:59 GMT ;path=/";
 $('body').css( "background-color", "black");
 $('body').css( "color", "white");
 $('.darkmode-text').text("Darkmode deaktivieren");
  }
  if (color === "white") {
 $('body').css( "background-color", "white")
 $('body').css( "color", "black")
 $('.darkmode-text').text("Darkmode aktivieren");
  document.cookie = "darkmode=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  }
  }

if ($('#Verbindungstable td').length == 0) {
   $('#Verbindungen').css( "display", "none" );
   $('#Details').css("display","none");
}

</script>