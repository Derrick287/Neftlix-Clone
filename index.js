function toggleContent(itemId) {
  var content = document.getElementById("content" + itemId);
  var svgPath = document.getElementById("svg-path-" + itemId);

  // Close all other contents and reset SVGs
  var contents = document.getElementsByClassName("item-content");
  for (var i = 0; i < contents.length; i++) {
    if (contents[i].id !== "content" + itemId) {
      contents[i].style.display = "none";
    }
  }

  // Toggle the clicked content
  content.style.display = content.style.display === "block" ? "none" : "block";

  // Toggle SVG between plus and X
  if (contents.style.display === "block") {
    svgPath.setAttribute("d", "M7 7L17 17M17 7L7 17"); // X shape
  } else {
    svgPath.setAttribute("d", "M11 11V2H13V11H22V13H13V22H11V13H2V11H11Z"); // Plus shape
  }
}