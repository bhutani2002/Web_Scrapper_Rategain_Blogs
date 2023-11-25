import React, { useState } from 'react'
import { Download } from 'lucide-react';
import axios from 'axios';
import portData from '../port.json'; 
const Scrape_Body = () => {
    const [port, setPort] = useState(portData.PORT);
    const [candownload, setCandownload] = useState(false);
    async function handleScrape(){
        try {
            const response = await axios.get(`http://127.0.0.1:${port}/start`);
            setCandownload(true);
            // console.log(response.data.data)
          } catch (error) {
            console.error('Error searching Blog_api', error);
          }
    }
    const handleDownload = async() => {
        const response = await axios.get(`http://127.0.0.1:${port}/download_excel`, {
            responseType: 'blob',
        });
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'Blogs_Data.xlsx');
    
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      };    
  return (
    <div className='flex-col justify-center items-center'>
        <div className="scrape_content flex-col justify-center items-center p-24">
            <div className='flex justify-center items-center text-justify text-[35px] font-bold mb-4'>
                <p>Begin scraping blog data from RateGain's blogs.</p>
            </div>
            <div className='flex justify-center items-center space-x-32'>
                <button
                    disabled = {candownload}
                    onClick={handleScrape}
                    className={!candownload ? "text-white rounded-[10px] text-[20px] py-4 px-12 bg-black" : " text-white rounded-[10px] text-[20px] py-4 px-12 bg-[rgb(56,56,56)]"}
                >
                    Scrape Data
                </button>
                <button
                    disabled = {!candownload}
                    onClick={handleDownload}
                    // style={{ background: 'linear-gradient(to right, rgb(0, 0, 0), rgb(105,105,105)' }
                    className={!candownload ?" text-white rounded-[10px] text-[20px] py-4 px-12 flex justify-center items-center bg-[rgb(56,56,56)]": "text-white rounded-[10px] text-[20px] py-4 px-12 flex justify-center items-center bg-black"}
                >
                    <span className='mr-4'><Download/></span>Download Extracted Data
                </button>
            </div>
        </div>
    </div>
  )
}

export default Scrape_Body