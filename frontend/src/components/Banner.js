import React from 'react'
import Banner_picture from '../assets/Rategain_Banner_Web.jpg'
const Banner = () => {
  return (
    <div className = "w-full h-[420px]" style={{ backgroundImage: `url(${Banner_picture})`, objectFit: 'contain', backgroundPosition: 'center', zIndex: '-1'}}>
        <div className='absolute top-36 right-1/4 text-[50px] z-40 text-white w-[920px]'>
            <p>Unveiling insights in the code of the web.</p>
        </div>
    </div>
  )
}

export default Banner