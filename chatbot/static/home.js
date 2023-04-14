$(document).on('submit', '#prompt', function(e){
    e.preventDefault(); // prevent the page from reloading
    $.ajax({
        type: 'POST',
        url: "",
        data: {
            message: $('#prmpt').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }
    });
    $( ".parent" ).load(window.location.href + " .parent" );
})

$(document).ready(function(){
    setInterval(function(){
        $( ".test" ).load(window.location.href + " .test" );

    }, 1000)
})