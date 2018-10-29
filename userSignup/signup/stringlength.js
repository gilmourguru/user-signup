function stringlength(username, password1, password2, minlength, maxlength)
{ 
var username = username.value; 
var password1 = password1;
var password2 = password2;
var mnlen = minlength;
var mxlen = maxlength;

    if (username.length < mnlen || username.length > mxlen) {
        alert("Please input a username between " + mnlen + " and " + mxlen + " characters");
        return false;
    }
    else if (password1.length < mnlen || password1.length > mxlen) {
        alert('Please input a password between " + mnlen + " and " + mxlen + " characters');
        return false;
    }
    else {
        return true;
    }
}
