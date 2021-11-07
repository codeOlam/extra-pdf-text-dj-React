import { useState, useEffect } from "react";
import axios from "axios";

const extract_url = "http://127.0.0.1:8000/api/extracted_text/";

type DocArrType = {
  id: number;
  title: string;
  pdf_doc: string;
};

const ExtractText = () => {
  const [text, setText] = useState<DocArrType>();

  useEffect(() => {
    fetchText();
  }, []);

  const fetchText = async () => {
    try {
      const { data } = await axios.get(extract_url);
      console.log("[fetchText] data: ", data.id);
      setText(data);
      console.log("[fetchText] text:", text?.id);
    } catch (error) {
      throw error;
    }
  };

  return (
    <div>
      <div>Extracted Text is: </div>
      <div>
        <p>id: {text?.id}</p>
        <p>title: {text?.title}</p>
        <p>pdf_doc: {text?.pdf_doc}</p>
      </div>
    </div>
  );
};

export default ExtractText;
