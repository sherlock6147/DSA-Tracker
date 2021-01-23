var menuBtn = document.getElementById('menu-btn');
var navMenu = document.getElementById('main-nav');
menuBtn.addEventListener("click", function () {
    navMenu.classList.toggle("invisible");
});
// var data = JSON.parse("");
//     
    
fetch('Outputs/listOfProblems.json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    var statusHTML = '';
      for (var i = 0; i < data.length; ++i) {
        statusHTML += '<tr>';
        statusHTML += '<td>' + data[i].topic + '</td>';
        statusHTML += '<td>' + data[i].problemStatement + '</td>';
        statusHTML += '<td>' + data[i].status + '</td>';
        statusHTML += '</tr>';
    }
    $('tbody').html(statusHTML);    
  })
  .catch(function (err) {
    console.log(err);
  });