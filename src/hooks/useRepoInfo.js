import { useEffect, useState } from "react"
import { eel } from "../eel"

const useRepoInfo = () => {
    const [info , setInfo] = useState([] || localStorage.getItem("repoInfo").split(','))
    const dirValue = localStorage.getItem("dirValue")
    useEffect(() => {
        eel.getInfo(dirValue)(ret => {
            setInfo(ret)
        })
    },[])
    return [info , setInfo]
}

export default useRepoInfo