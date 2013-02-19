<?php
  // Remember to copy files from the SDK's src/ directory to a
  // directory in your application on the server, such as php-sdk/
  require_once('facebook.php');

  $config = array(
    'appId' => '156425604515025',
    'secret' => '1a7a7e03f2909e009471624ae1378587',
  );

  $facebook = new Facebook($config);
  $user_id = $facebook->getUser();
?>
<html>
  <head></head>
  <body>

  <?php
    if($user_id) {

      // We have a user ID, so probably a logged in user.
      // If not, we'll get an exception, which we handle below.
      try {
          
          
       
        $user_profile = $facebook->api('/me?fields=likes','GET');
        $interestst = array();
        if(isset($user_profile['likes']['data'])){
        for($i=0;$i<sizeof($user_profile['likes']['data']);$i++)
        if(isset($interestst[$user_profile['likes']['data'][$i]["category"]]))
            $interestst[$user_profile['likes']['data'][$i]["category"]]++;
        else
            $interestst[$user_profile['likes']['data'][$i]["category"]]=1;
        
       //for($i=0;$i<sizeof($interestst);$i++)
           echo print_r($interestst);
        }
        else
            echo "None";

      } catch(FacebookApiException $e) {
        // If the user is logged out, you can have a 
        // user ID even though the access token is invalid.
        // In this case, we'll get an exception, so we'll
        // just ask the user to login again here.
        $login_url = $facebook->getLoginUrl(); 
        echo 'Please <a href="' . $login_url . '">login.</a>';
        error_log($e->getType());
        error_log($e->getMessage());
      }   
    } else {

      // No user, print a link for the user to login
      $login_url = $facebook->getLoginUrl();
      echo 'Please <a href="' . $login_url . '">login.</a>';

    }

  ?>

  </body>
</html>