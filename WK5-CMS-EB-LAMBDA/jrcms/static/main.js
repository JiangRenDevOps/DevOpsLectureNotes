$(".dropdown-menu a").click(function(){
    var item = $(this).text();
    loadContent(item);
 });

$('#updateButton').click(function() {
    $.ajax({
        url: '/content',
        type: 'PUT',
        data: {'contentValue' : $('#contentValue').val(), 'contentKey': $('#contentKey').text().trim()}
      });
    console.log("update button clicked.")
});

function loadContent(item) {
    $('#contentKey').text(item);
    localStorage.setItem("contentKey", item);
    $.get( "/content?contentKey="+item, function( data ) {
        $("#contentValue").val(data);
        console.log(data)
    });    
}

var contentKey = localStorage.getItem("contentKey")
if (!contentKey) {
    contentKey = "Default"
}
loadContent(contentKey);
