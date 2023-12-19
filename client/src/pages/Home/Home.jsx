import Navbar from "../../components/navbar/Navbar";
import plantImge1 from "../../assets/plant1.png";
import plantImge2 from "../../assets/plant2.png";

function Home() {
  return (
    <div className="fixed h-screen w-full bg-lime-50">
      <div className="absolute grid grid-cols-3 inherit justify-center items-center pl-32 p-20">
        <div className="w-96">
          <h1 className="font-extrabold text-5xl">
            Nausicca's <span className="text-green-400">Green</span>
          </h1>
          <p className="pt-6">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus
            aspernatur ad eveniet quas laborum in quisquam sequi ipsa totam
            aperiam autem delectus provident officia, dicta perspiciatis
            voluptates, voluptatem veniam commodi.
          </p>
          <img
            className="h-auto cursor-pointer hover:drop-shadow-2xl bg-clip-border"
            src={plantImge2}
            alt="plant2"
            srcSet=""
          />
          {/* <div className="flex w-full justify-around items-center">
            <div className="bg-lime-200 border-2 p-1">Grant</div>
            <div className="bg-lime-200 border-2 p-2">grant</div>
          </div> */}
        </div>
        <div className="h-20 w-20 rounded-full bg-green-200">
          <div className="h-10 w-10 rounded-full bg-green-400 "></div>
        </div>
        <div className="h-auto rounded-xl z-50">
          <img
            className="cursor-pointer hover:drop-shadow-2xl bg-clip-border"
            src={plantImge1}
            alt="plant1"
          />
          <div className="h-40 bottom-0 rounded-md right-0 bg-[#55A785]"></div>
        </div>
      </div>
    </div>
  );
}

export default Home;
