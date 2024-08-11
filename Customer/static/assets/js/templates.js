$(document).ready(function(){
    $(".Search").click(function(){
        var searchValue = document.getElementById('searchInput').value();// گرفتن مقدار ورودی از انپوت
        var form = document.getElementById('searchForm');
        form.submit();
    })
    $(".Edit").click(function(){
        alert("سلام")
    })
    

})

function Delete(value){
        document.getElementById("deleteItem").href=value
}

function Deletemessage(value){
    document.getElementById("deletemessage").href=value
}

$("#MortgageAndRent").click(function(){
    $("#commercial").hide()
})

$("#mortgage").click(function(){
    $("#Villa").hide()
    $("#commercial").hide()
})
$("#exchange").click(function(){
    $("#office").hide()
    $("#Apparatus").hide()
    $("#commercial").hide()
})

