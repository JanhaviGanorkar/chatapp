import React from 'react';

const About = () => {
  const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  return (
    <>
      {/* <div className="bg-slate-500 text-white"> */}
      <div class="text-white absolute inset-0 -z-10 h-full w-full items-center px-5 py-24 [background:radial-gradient(125%_125%_at_50%_10%,#000_40%,#63e_100%)]">
      <div class="absolute top-0 -z-10 h-full w-full bg-white"><div class="absolute bottom-auto left-auto right-0 top-0 h-[500px] w-[500px] -translate-x-[30%] translate-y-[20%] rounded-full bg-[rgba(173,109,244,0.5)] opacity-50 blur-[80px]">
        
        
      <h1 >dsfjalo</h1>
        </div></div>
      {/* <Button>aefe</Button> */}
      {num.map((n) => (
        <div key={n}>
          <p>Number: {n}</p>
        </div>
      ))}
    </div >

    <div class="absolute top-0 -z-10 h-full w-full text-gray-950 bg-white"><div class="absolute bottom-auto left-auto right-0 top-0 h-[500px] w-[500px] -translate-x-[30%] translate-y-[20%] rounded-full bg-[rgba(173,109,244,0.5)] opacity-50 blur-[80px]">
      <p>Welcome</p>
      <h1>hello</h1>
      </div></div>
    </>
  );
};

export default About;


// https://in.pinterest.com/pin/92957179803392576/