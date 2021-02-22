import React from 'react'
import Button from '../components/button'
import {useHistory} from 'react-router-dom'
const Splash = () => {
    const history = useHistory()
    const nextPage = () => {
    let page = '/home'
    history.push(page)
    }
    return (
        <>
            <h1>Splash Screen</h1>
            <Button text='Splash' onClick = {nextPage}/>
        </>
    );
}

export default Splash

