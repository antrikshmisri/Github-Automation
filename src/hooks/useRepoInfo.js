import { useEffect, useState } from "react"
import { eel } from "../eel"

const useRepoInfo = () => {
    const [info, _setInfo] = useState([] || localStorage.getItem("repoInfo").split(','))
    const dirValue = localStorage.getItem("dirValue")
    useEffect(() => {
        eel.getInfo(dirValue)(ret => {
            _setInfo(ret)
        })
    }, [dirValue])

    const setInfo = (info) => {
        _setInfo(info)
        localStorage.setItem("repoInfo", info.join(','))
    }
    return [info, setInfo]
}

export default useRepoInfo