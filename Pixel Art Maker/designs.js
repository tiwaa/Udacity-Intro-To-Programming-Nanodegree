// Select color input
const color = $('#colorPicker').val();

// Select size input
$('#sizePicker').submit(function getDimension(evt){
    evt.preventDefault();
    let h = $('#inputHeight').val();
    let w = $('#inputWidth').val();
    makeGrid(h, w);
});
// When size is submitted by the user, call makeGrid()

// Your code goes here!
function makeGrid(m, n) {
    $('tr').remove();
    for (var u = 1; u<= m; u++){
        $('#pixelCanvas').append('<tr id=table' + u + '></tr>')
        for (var v = 1; v<= n; v++){
        $('#table' + u).append('<td></td>');
        }
    }
}

//color cell
$('td').click(function colorCell(){
    if($(this).css('background-color')){
        $(this).removeAttr('style');
    }else{
    $(this).css('background-color', color);
    }
});

