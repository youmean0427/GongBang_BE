import { useMutation } from "@tanstack/react-query";
import React, {useState} from "react"
import { getCoffeeCafeDetailReviewCreateAPI } from "../apis/api";
import { useParams } from "react-router-dom";

export default function ReviewCreate() {

    const [inputs, setInputs] = useState({
        title : "title",
        content : "content",
        date : "2023-12-29",
        score : "5",
        type : "1",
        user : "test"
    })
    const [imageList, setImageList] = useState([]);
    
    const onChange = (e) => {
        const {name, value} = e.target
        setInputs({
            ...inputs,
            [name] : value
        })
    }
    console.log(inputs)

    const onClick = () => {
        const formData = new FormData();
        formData.append('title', inputs.title);
        formData.append('content', inputs.content);
        formData.append('date', inputs.date);
        formData.append('score', inputs.score);
        formData.append('type', inputs.type);
        formData.append('user', inputs.user);
        for (let i = 0; i < imageList.length; i++) {
            formData.append('image', imageList[i]);
        }
        // * FormData Check *
        for (let value of formData.values()) {
            console.log(value)
        }

        reviewCreateMutation.mutate(formData)

    }
    const { id } = useParams();

    const reviewCreateMutation = useMutation
    (['getCoffeeCafeDetailReviewCreateAPI'],
    (formData) => getCoffeeCafeDetailReviewCreateAPI(id, formData),
    {
        onSuccess: (res) => {
            console.log(res, "Success")
        },
        onError : (res) => {
            console.log(res, "Error")
        }
    }
     )
    
    const handleImageChange = (event) => {
        const files = event.target.files;
        let imageUrl = []
        for (let i = 0; i < files.length; i++) {
            imageUrl.push(files[i])
            // * Blob *
            // imageUrl.push(URL.createObjectURL(files[i]))
        }
        setImageList(imageUrl)
    };



    return (
        <>
        <div>
           <div>제목</div>
           <div><input name = "title" onChange={onChange}/></div>
           <div>내용</div> 
           <div><input name = "content" onChange={onChange}/></div>
           <div>날짜</div> 
           <div><input name = "date" onChange={onChange}/></div>
           <div>점수</div>
           <div><input name = "score" onChange={onChange}/></div>
           <div>타입</div>
           <div><input name = "type" onChange={onChange}/></div>
           <div>타입</div>
           <div><input name = "user" onChange={onChange}/></div>
           <div>사진</div>
           <div>
            <input type="file" accept="image/*" onChange= {handleImageChange}/>

           </div>
        </div>
        <div><button onClick={onClick}>제출</button></div>

        
        </>
    )
}