$.ajax({
  method: "GET",
  url: "api/buses",
  dataType: "JSON",
  success: function(data) {
    console.log(data);
  }
});
