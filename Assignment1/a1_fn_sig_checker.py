<!DOCTYPE html>
<html>
  	<head>
    	<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="/css/opensans.css" media="screen, handheld" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>UW NetID sign-in</title>
  <meta name="description" content="">
  <meta name="author" content="">
<meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta http-equiv="cleartype" content="on">
<link rel="stylesheet" type="text/css" href="/css/weblogin-global.css" media="screen, handheld" />
  <link rel="stylesheet" type="text/css" href="/css/weblogin-enhanced.css" media="screen  and (min-width: 40.5em)" />
  <!--[if (lt IE 9)&(!IEMobile)]>
  <link rel="stylesheet" type="text/css" href="/css/weblogin-enhanced.css" />
  <![endif]-->


<script>
function _clear_screen() {
   docdiv = document.getElementById('main');
   docdiv.className='visuallyhidden';
}
/* Allow @uw.edu and @washington.edu, but reject any other @something.
   On password retry, focus on the password field. */
window.onload = function() {
  document.forms[0][0].focus();
  document.getElementById('idplogindiv').onsubmit=function(e) {
   id = document.getElementById("weblogin_netid").value.toLowerCase();
   document.getElementById("weblogin_netid").value = id;
   at = id.indexOf("@");
   if (at<0) {
      _clear_screen();
      return true;
   }
   if (id.substr(at)=="@uw.edu" || id.substr(at)=="@washington.edu" || id.substr(at)=="@u.washington.edu") {
      document.getElementById("weblogin_netid").value = id.substr(0,at);
      _clear_screen();
      return true;
   }
   document.getElementById("uwsignin").innerHTML = 'Please sign in with your <span style="color: #600000" text-decoration: underline;">UW NetID</span>';
   return false;
}}


</script>
  	</head>


<body>

  <h1 class="visuallyhidden">UW NetID sign-in</h1>

  <div id="container">
    <div id="main" role="main">

        <h2 class="visuallyhidden" aria-flowto="weblogin_warning">Login</h2>
        <div class="form">
          <div><img src="/img/weblogin.png" height="57" width="198" alt="" aria-hidden="true"></div>

            
  <p id="uwsignin">Please sign in.</p>

            <!-- "Please sign in" is included in the error vm -->

          <form name="idplogin" id="idplogindiv" method="POST" action="/idp/profile/SAML2/Redirect/SSO;jsessionid=B3C1E649D6319A7B599EED28D9182C45.idp07?execution=e1s1" autocomplete="off">

            <ul class="login">
              <li><label for="weblogin_netid">UW NetID:</label>
                   <input id="weblogin_netid" placeholder="UW NetID" type="text" NAME="j_username" SIZE="20"
                       autocorrect="off" autocapitalize="none"
                      value=""/></li>
              <li><label for="weblogin_password">Password:</label>
                   <input id="weblogin_password" placeholder="Password" type="password" NAME="j_password" SIZE="20" /></li>
                         <li><a href="https://identity.uw.edu/account/resetpassword/">Forgot your password?</a></li>
                   </ul>

            <ul class="submit">
              <li><input type="submit" id="submit_button" name="_eventId_proceed" value="Sign in"></li>
            </ul>

            </form>

        </div>

        <h2 class="visuallyhidden">UW NetID Help</h2>
        <div class="sidebar">

                <!-- <h3 style="margin-top:0;">UW NetID Help</h3> -->

            <ul class="links">
                <li><a href="http://itconnect.uw.edu/security/uw-netids/about-uw-netids/account-recovery//">Learn about account recovery options</a></li>
                <li><a href="http://itconnect.uw.edu/security/uw-netids/about-uw-netids/">Learn about UW NetIDs</a></li>
                <li><a href="http://itconnect.uw.edu/security/uw-netids/weblogin/">Learn about UW NetID sign-in</A></li>
                <li><a href="https://uwnetid.washington.edu/newid/">Obtain a UW NetID</a></li>
                <li style="height: 30px"></li>
                <li><a href="http://itconnect.uw.edu/help/">Need help?</a></li>
            </ul>

        </div>
        <div id="weblogin_warning" class="warning">

            <p>Sign in reduces how often you have to reauthenticate to access UW resources.</p>

            <p>Learn how to <a href="http://itconnect.uw.edu/security/uw-netids/weblogin/#logout">sign out</a> at the end of your browsing session.</p>

            <p class="copyright"><span class="copyright-links"><a href="http://www.washington.edu/online/privacy">PRIVACY</a> | <a href="http://www.washington.edu/online/terms">TERMS</a></span></p>

         </div>


    </div> <!--end main -->
  </div> <!-- end container -->


 	</body>
</html>
