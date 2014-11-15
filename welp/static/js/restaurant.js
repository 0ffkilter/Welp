function generate_phrase(convince_level) {
  var data = words;
  var phrase = generate_food(convince_level, data);
  if (Math.random() < (convince_level * 0.3)) {
    phrase = phrase.concat(generate_service(convince_level, data));  
  }
  if (Math.random() < (convince_level * 0.3)) { 
    phrase = phrase.concat(generate_other(convince_level, data));
  }
  return phrase
}

function generate_food(convince_level, data) {
  return "  The food was ".concat(data[convince_level]["food"][Math.floor(Math.random() *
  (data[convince_level]["food"].length))]).concat(".");
}

function generate_service(convince_level, data) {
  return "  Also, The service was ".concat(data[convince_level]["service"][Math.floor(Math.random() *
  (data[convince_level]["service"].length))]).concat(".");
}

function generate_other(convince_level, data) {
  return "  I'd also like to say that the ".concat(data["nouns"][Math.floor(Math.random() * data["nouns"].length)] + 
          " was ").concat(data[convince_level]["other"][Math.floor(Math.random()*data[convince_level]["other"].length)]).concat(".");
}

function generate_name() {
  return generate_first().concat(generate_last());
}

function generate_first() {
  return "Steve";
}

function generate_last() {
  return " Smith";
}

function create_comment(level) {
  var div = document.createElement("div");
  div.className = "review";
  var header = document.createElement("h6");
  header.appendChild(document.createTextNode(generate_name()));
  div.appendChild(header);
  var body = document.createElement("p");
  body.appendChild(document.createTextNode(generate_phrase(level)))
  div.appendChild(body);
  document.body.appendChild(div);

}
function convinceMe() { 
  var num = Math.floor(Math.random() * 5 + 1);
  var i = 0;
  for (i = 0; i < num; i++) {
    create_comment(1);
  }
}

