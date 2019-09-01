// listener for Enter keypress
$(document).ready(function(){
    $('#play_form').keypress(function(e){
      if(e.keyCode==13) // Press Enter key
        $('#play_button').click();
    });
});

// onclick for play button
$(function() {
  $('a#play_button').bind('click', function() {
    $.get('/api/play', {bet: document.getElementById("bet_input").value, wager: document.getElementById("wager_input").value},
        function(data) {
          console.log(data)
          $("#req_display_text").text(JSON.stringify(JSON.parse(data), null, 2))
    }, "text");
    return false;
  });
});
