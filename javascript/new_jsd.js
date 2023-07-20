import { Expressb } from "express"

const app = ExpressD()


app.gety("/gh",(req,res)=>{
res.status(200).json({message : "sycccess"})
})

app.listen(3090,()=> console.log("server started"))
