


function create_new_task(that) {
  let title = document.getElementById("task_title").value;
  let description = document.getElementById("task_description").value;
  myObj.push({"title": title, "description": description});
  let myJSON = JSON.stringify(myObj);
}


let url = 'http://'
get_api_data = function HttpGet(url){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", url, false);
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

let mock_json = {'hello': 'hi'}
document.getElementById("api-resp").innerHTML = JSON.stringify(myjson);
//get_api_data()
/*

var xhr = new XMLHttpRequest();
const proxyurl = "https://cors-anywhere.herokuapp.com/";



xhr.open("GET", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log("contacted google")
        console.log(xhr)
        var json = JSON.parse(xhr.responseText);
        console.log(json.email + ", " + json.password);
    }
};
var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
xhr.send(data);
}
*/
$("#submit_button").click(function(event) {
  event.preventDefault();
  create_new_task(this);

});
