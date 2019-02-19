

var myObj = [];

/*window.location = "demo_json.php?x=" + myJSON;*/

function create_new_task() {
  //take in student variables from form
  let title = document.getElementById("task_title").value;
  // let description = document.getElementById("task_description").value;
  // myObj.push({"title": title, "description": description});
  // var myJSON = JSON.stringify(myObj);
  // console.log(myJSON);
  console.log(title)
}

$("#submit_button").click(function(event) {
  create_new_task();
});
