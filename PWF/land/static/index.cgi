<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
                      "http://www.w3.org/TR/html4/loose.dtd">
<html>
  <head>
    <title>Bugzilla Main Page</title>


<link rel="Top" href="https://bugzilla.mozilla.org/">



    
    
    <link href="skins/standard/global.css?1311936950"
          rel="alternate stylesheet" 
          title="Classic"><link href="skins/standard/global.css?1311936950" rel="stylesheet"
        type="text/css" ><link href="skins/standard/index.css?1286523130" rel="stylesheet"
        type="text/css" ><!--[if lte IE 7]>
      



  <link href="skins/standard/IE-fixes.css?1304660014" rel="stylesheet"
        type="text/css" >
<![endif]-->

    <link href="skins/contrib/Dusk/global.css?1311936950" rel="stylesheet"
        type="text/css" title="Dusk"><link href="skins/contrib/Dusk/index.css?1286523130" rel="stylesheet"
        type="text/css" title="Dusk">
<link href="skins/contrib/Dusk-Helvetica/global.css?1311936950" rel="alternate stylesheet"
        type="text/css" title="Dusk-Helvetica"><link href="skins/contrib/Dusk-Helvetica/index.css?1311936950" rel="alternate stylesheet"
        type="text/css" title="Dusk-Helvetica"><link href="skins/contrib/Dusk-Segoe/global.css?1311936950" rel="alternate stylesheet"
        type="text/css" title="Dusk-Segoe"><link href="skins/contrib/Dusk-Segoe/index.css?1311936950" rel="alternate stylesheet"
        type="text/css" title="Dusk-Segoe">

    

    <link href="skins/custom/global.css?1327393475" rel="stylesheet"
        type="text/css" ><link href="skins/custom/index.css?1303571902" rel="stylesheet"
        type="text/css" ><!--[if lte IE 7]>
      



  <link href="skins/custom/IE-fixes.css?1303944011" rel="stylesheet"
        type="text/css" >
<![endif]-->

    
<script type="text/javascript" src="js/yui/yahoo-dom-event/yahoo-dom-event.js?1303753510"></script><script type="text/javascript" src="js/yui/cookie/cookie-min.js?1303753510"></script><script type="text/javascript" src="js/global.js?1303571902"></script>

    <script type="text/javascript">
    <!--
        YAHOO.namespace('bugzilla');
        YAHOO.util.Event.addListener = function (el, sType, fn, obj, overrideContext) {
               if ( ("onpagehide" in window || YAHOO.env.ua.gecko) && sType === "unload") { sType = "pagehide"; };
               var capture = ((sType == "focusin" || sType == "focusout") && !YAHOO.env.ua.ie) ? true : false;
               return this._addListener(el, this._getType(sType), fn, obj, overrideContext, capture);
         };
        if ( "onpagehide" in window || YAHOO.env.ua.gecko) {
            YAHOO.util.Event._simpleRemove(window, "unload", 
                                           YAHOO.util.Event._unload);
        }
        
        function unhide_language_selector() { 
            YAHOO.util.Dom.removeClass(
                'lang_links_container', 'bz_default_hidden'
            ); 
        } 
        YAHOO.util.Event.onDOMReady(unhide_language_selector);

        
        var BUGZILLA = {
            param: {
                cookiepath: '\/',
                maxusermatches: 100
            },
            constant: {
                COMMENT_COLS: 80
            },
            string: {
                

                attach_desc_required:
                    'You must enter a Description for this attachment.',
                component_required:
                    'You must select a Component for this bug.',
                description_required:
                    'You must enter a Description for this bug.',
                short_desc_required:
                    'You must enter a Summary for this bug.',
                version_required:
                    'You must select a Version for this bug.'
            }
        };

    // -->
    </script>


    

    
    <link rel="search" type="application/opensearchdescription+xml"
                       title="Bugzilla@Mozilla" href="./search_plugin.cgi"><link rel="shortcut icon" href="extensions/BMO/web/images/favicon.ico">

<style type="text/css">
body {
  background: url("extensions/BMO/web/images/background.png") repeat-x;
}
</style><meta name="robots" content="noarchive">
  </head>



  <body onload=""
        class="bugzilla-mozilla-org yui-skin-sam">



<div id="header">
<div id="banner">
  </div>

<table border="0" cellspacing="0" cellpadding="0" id="titles">
<tr>
    <td id="title">
      <p>Bugzilla@Mozilla &ndash; Main Page</p>
    </td>


    <td id="information">
      <p class="header_addl_info">version 4.0.4+</p>
    </td>
</tr>
</table>

<table id="lang_links_container" cellpadding="0" cellspacing="0"
       class="bz_default_hidden"><tr><td>
</td></tr></table>
<ul class="links">
  <li><a href="./">Home</a></li>
  <li><span class="separator">| </span><a href="enter_bug.cgi">New</a></li>
  <li><span class="separator">| </span><a href="describecomponents.cgi">Browse</a></li>
  <li><span class="separator">| </span><a href="query.cgi">Search</a></li>

  <li class="form">
    <span class="separator">| </span>
    <form action="buglist.cgi" method="get"
        onsubmit="if (this.quicksearch.value == '')
                  { alert('Please enter one or more search terms first.');
                    return false; } return true;">
    <input class="txt" type="text" id="quicksearch_top" name="quicksearch" 
           value="">
    <input class="btn" type="submit" value="Search" 
           id="find_top"></form>
  <a href="page.cgi?id=quicksearch.html" title="Quicksearch Help">[?]</a></li>

  <li><span class="separator">| </span><a href="report.cgi">Reports</a></li>

  <li>
      <span class="separator">| </span>
        <a href="request.cgi">Requests</a></li>

  
    
      <li id="new_account_container_top">
        <span class="separator">| </span>
        <a href="createaccount.cgi">New&nbsp;Account</a>
      </li>

    <li id="mini_login_container_top">
  <span class="separator">| </span>
  <a id="login_link_top" href="https://bugzilla.mozilla.org/index.cgi?GoAheadAndLogIn=1"
     onclick="return show_mini_login_form('_top')">Log In</a>
  <form action="https://bugzilla.mozilla.org/index.cgi" method="POST" 
        class="mini_login bz_default_hidden"
        id="mini_login_top"
        onsubmit="return check_mini_login_fields( '_top' );"
  >
    <input id="Bugzilla_login_top" 
           class="bz_login"
           name="Bugzilla_login"
           onfocus="mini_login_on_focus('_top')"
    >
    <input class="bz_password" 
           id="Bugzilla_password_top" 
           name="Bugzilla_password"
           type="password"
    >
    <input class="bz_password bz_default_hidden bz_mini_login_help" type="text" 
           id="Bugzilla_password_dummy_top" value="password"
           onfocus="mini_login_on_focus('_top')"
    >
      <input type="checkbox" id="Bugzilla_remember_top" 
             name="Bugzilla_remember" value="on" class="bz_remember"
                 checked>
      <label for="Bugzilla_remember_top">Remember</label>
    <input type="submit" name="GoAheadAndLogIn" value="Log in" 
            id="log_in_top">
    <script type="text/javascript">
      mini_login_constants = {
          "login" : "email address",
          "warning" : "You must set the email address and password before logging in."
      };
      
      if (YAHOO.env.ua.gecko || YAHOO.env.ua.ie || YAHOO.env.ua.opera) {
          YAHOO.util.Event.onDOMReady(function() {
              init_mini_login_form('_top');
          });
      }
      else {
          YAHOO.util.Event.on(window, 'load', function () {
              window.setTimeout(function() {
                  init_mini_login_form('_top');
              }, 200);
          });
    }
    </script>
    <a href="#" onclick="return hide_mini_login_form('_top')">[x]</a>
  </form>
</li>
<li id="forgot_container_top">
  <span class="separator">| </span>
  <a id="forgot_link_top" href="https://bugzilla.mozilla.org/index.cgi?GoAheadAndLogIn=1#forgot"
     onclick="return show_forgot_form('_top')">Forgot Password</a>
  <form action="token.cgi" method="post" id="forgot_form_top"
        class="mini_forgot bz_default_hidden">
    <label>Login: <input type="text" name="loginname" size="20"></label>
    <input id="forgot_button_top" value="Reset Password" 
           type="submit">
    <input type="hidden" name="a" value="reqpw">
    <a href="#" onclick="return hide_forgot_form('_top')">[x]</a>
  </form>
</li>
</ul>
</div> 

<div id="bugzilla-body">


<script type="text/javascript">
<!--
function onLoadActions() {
  quicksearchHelpText('quicksearch_main', 'show');
  if( window.external.AddSearchProvider ){
    YAHOO.util.Dom.removeClass('quicksearch_plugin', 'bz_default_hidden');
  }
  document.getElementById('quicksearch_top').focus();
}
function addSidebar() {
  var sidebarname=window.location.host;
  if (!/bug/i.test(sidebarname))
    sidebarname="Bugzilla "+sidebarname;
  window.sidebar.addPanel (sidebarname, "https://bugzilla.mozilla.org/sidebar.cgi", "");
}
var quicksearch_message = "Enter a bug # or some search terms";

function checkQuicksearch( form ) {
  if (form.quicksearch.value == '' || form.quicksearch.value == quicksearch_message ) { 
    alert('Please enter one or more search terms first.');
    return false; 
  }
  return true;         
}

function quicksearchHelpText(el_id, action){
  var el = document.getElementById(el_id);
  if ( action == "show") {
    if( el.value == "" ) {
      el.value = quicksearch_message
      YAHOO.util.Dom.addClass(el, "quicksearch_help_text");
    }
  } else {
    if( el.value == quicksearch_message ) {
      el.value = "";
      YAHOO.util.Dom.removeClass(el, "quicksearch_help_text");
    }
  }
}
YAHOO.util.Event.onDOMReady(onLoadActions);
//-->
</script>


<div id="page-index">
  <table>
    <tr>
      <td>
        <h1 id="welcome"> Welcome to Bugzilla</h1>
        <div class="intro"><a id="get_help" class="bz_common_actions"
   href="page.cgi?id=get_help.html"><span>Get Help</span></a></div>
        <a id="enter_bug" class="bz_common_actions"
           href="enter_bug.cgi"><span>File a Bug</span></a>
      
        <a id="query" class="bz_common_actions" 
           href="query.cgi"><span>Search</span></a>
      
        <a id="account" class="bz_common_actions"
            href="createaccount.cgi"><span>Open a New Account</span></a>

        <form id="quicksearchForm" name="quicksearchForm" action="buglist.cgi"
              onsubmit="return checkQuicksearch(this);">
          <div>
            <input id="quicksearch_main" type="text" name="quicksearch"
              onfocus="quicksearchHelpText(this.id, 'hide');"
              onblur="quicksearchHelpText(this.id, 'show');"
            >
            <input id="find" type="submit" value="Quick Search">
            <ul class="additional_links" id="quicksearch_links">
              <li>
                <a href="page.cgi?id=quicksearch.html">Quick Search help</a>
              </li>
              <li class="bz_default_hidden" id="quicksearch_plugin">
                |
                <a href="javascript:window.external.AddSearchProvider('https://bugzilla.mozilla.org/search_plugin.cgi')">
                 Install the Quick Search plugin
                </a>
              </li>
            </ul>
            <ul class="additional_links">
              <li>
                <a href="http://www.bugzilla.org/docs/4.0/en/html/using.html">Bugzilla User's Guide</a>
              </li>
              <li>
                |
                <a href="page.cgi?id=release-notes.html">Release Notes</a>
              </li><li>
|
<a href="page.cgi?id=etiquette.html">Bugzilla Etiquette</a>
</li>
<li>
|
<a href="https://developer.mozilla.org/en/Bug_writing_guidelines">Bug Writing Guidelines</a>
</li>
            </ul>
          </div>
        </form>
        <div class="outro"></div>
      </td>
    </tr>
  </table>
</div>
</div>



<div id="footer">
  <div class="intro"></div>




<ul id="useful-links">
  <li id="links-actions"><ul class="links">
  <li><a href="./">Home</a></li>
  <li><span class="separator">| </span><a href="enter_bug.cgi">New</a></li>
  <li><span class="separator">| </span><a href="describecomponents.cgi">Browse</a></li>
  <li><span class="separator">| </span><a href="query.cgi">Search</a></li>

  <li class="form">
    <span class="separator">| </span>
    <form action="buglist.cgi" method="get"
        onsubmit="if (this.quicksearch.value == '')
                  { alert('Please enter one or more search terms first.');
                    return false; } return true;">
    <input class="txt" type="text" id="quicksearch_bottom" name="quicksearch" 
           value="">
    <input class="btn" type="submit" value="Search" 
           id="find_bottom"></form>
  <a href="page.cgi?id=quicksearch.html" title="Quicksearch Help">[?]</a></li>

  <li><span class="separator">| </span><a href="report.cgi">Reports</a></li>

  <li>
      <span class="separator">| </span>
        <a href="request.cgi">Requests</a></li>

  
    
      <li id="new_account_container_bottom">
        <span class="separator">| </span>
        <a href="createaccount.cgi">New&nbsp;Account</a>
      </li>

    <li id="mini_login_container_bottom">
  <span class="separator">| </span>
  <a id="login_link_bottom" href="https://bugzilla.mozilla.org/index.cgi?GoAheadAndLogIn=1"
     onclick="return show_mini_login_form('_bottom')">Log In</a>
  <form action="https://bugzilla.mozilla.org/index.cgi" method="POST" 
        class="mini_login bz_default_hidden"
        id="mini_login_bottom"
        onsubmit="return check_mini_login_fields( '_bottom' );"
  >
    <input id="Bugzilla_login_bottom" 
           class="bz_login"
           name="Bugzilla_login"
           onfocus="mini_login_on_focus('_bottom')"
    >
    <input class="bz_password" 
           id="Bugzilla_password_bottom" 
           name="Bugzilla_password"
           type="password"
    >
    <input class="bz_password bz_default_hidden bz_mini_login_help" type="text" 
           id="Bugzilla_password_dummy_bottom" value="password"
           onfocus="mini_login_on_focus('_bottom')"
    >
      <input type="checkbox" id="Bugzilla_remember_bottom" 
             name="Bugzilla_remember" value="on" class="bz_remember"
                 checked>
      <label for="Bugzilla_remember_bottom">Remember</label>
    <input type="submit" name="GoAheadAndLogIn" value="Log in" 
            id="log_in_bottom">
    <script type="text/javascript">
      mini_login_constants = {
          "login" : "email address",
          "warning" : "You must set the email address and password before logging in."
      };
      
      if (YAHOO.env.ua.gecko || YAHOO.env.ua.ie || YAHOO.env.ua.opera) {
          YAHOO.util.Event.onDOMReady(function() {
              init_mini_login_form('_bottom');
          });
      }
      else {
          YAHOO.util.Event.on(window, 'load', function () {
              window.setTimeout(function() {
                  init_mini_login_form('_bottom');
              }, 200);
          });
    }
    </script>
    <a href="#" onclick="return hide_mini_login_form('_bottom')">[x]</a>
  </form>
</li>
<li id="forgot_container_bottom">
  <span class="separator">| </span>
  <a id="forgot_link_bottom" href="https://bugzilla.mozilla.org/index.cgi?GoAheadAndLogIn=1#forgot"
     onclick="return show_forgot_form('_bottom')">Forgot Password</a>
  <form action="token.cgi" method="post" id="forgot_form_bottom"
        class="mini_forgot bz_default_hidden">
    <label>Login: <input type="text" name="loginname" size="20"></label>
    <input id="forgot_button_bottom" value="Reset Password" 
           type="submit">
    <input type="hidden" name="a" value="reqpw">
    <a href="#" onclick="return hide_forgot_form('_bottom')">[x]</a>
  </form>
</li>
</ul>
  </li>

  
    

  


  
</ul>

  <div class="outro"><a href="https://www.mozilla.org/about/policies/privacy-policy.html">Privacy Policy</a></div>
</div>
<script type="text/javascript" src="extensions/BMO/web/js/webtrends.js?1320921298"></script>
<script type="text/javascript">
//<![CDATA[
var _tag=new WebTrends({"dcsid":"dcsqjgr30wz5bd6zokoukhwj3_7z7z","rate":100,"fpcdom":"mozilla.org"});
_tag.dcsGetId();
//]]>
</script>
<script>
//<![CDATA[
_tag.dcsCollect();
//]]>
</script>
<noscript>
<div><img alt="DCSIMG" id="DCSIMG" width="1" height="1" src="//statse.webtrendslive.com/dcsqjgr30wz5bd6zokoukhwj3_7z7z/njs.gif?dcsuri=/nojavascript&amp;WT.js=No&amp;WT.tv=8.6.2"/></div>
</noscript>

</body>
</html>