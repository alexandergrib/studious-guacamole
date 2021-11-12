
let anonymous_checkbox = document.getElementById("anonymous_checkbox");

// if (anonymous_checkbox) {
//     console.log("anonymous_checkbox")
// }

anonymous_checkbox.addEventListener('change', function(){
    if ( this.checked) {
        console.log("checked");
    }else {
        console.log("unchecked");
    }
})