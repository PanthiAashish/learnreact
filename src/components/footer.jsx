import React from "react";

const date = new Date();


function Footer(){
    return <footer>
            <h1>{date.getFullYear()}</h1>
        </footer>
}

export default Footer;