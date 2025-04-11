import React, { useEffect, useState, useContext } from "react";
import { UserContext } from "../../Context";
import PrevNext from "../../PrevNext";
import InterestCard from "./InterestCard";

const InterestArray = [
  "Art", "Writing", "Reading", "Fashion", "Travel", "Sports", "Health", "Music",
  "Technology", "Movies", "Food", "Gaming", "Fitness", "Photography", "DIY",
  "Gardening", "Cooking", "Nature", "Animals", "Spirituality", "Finance",
  "Education", "History", "Science", "Cars", "Comedy", "Adventure", "Dance",
  "Volunteering", "Languages", "Anime", "Crafts", "Makeup", "Parenting",
  "Home Decor", "Astronomy", "Investing", "Politics", "Environment", "Podcasts",
  "Theater", "Board Games", "Magic", "Blogging", "Vlogging", "Coding",
  "Public Speaking", "Meditation", "Any",
];

const InterestInputStep = () => {
  const [selectedInterest, setInterest] = useState(undefined);
  const [activeInterest, setActiveInterest] = useState(null);
  const [alreadyFilled, setAlreadyFilled] = useState(false);
  const inputDetails = useContext(UserContext);

  const setSelectedInterest = (interest) => {
    inputDetails.userInput.interests = interest; // updated key
    setInterest(interest); // Update local state too
    setAlreadyFilled(true);
    console.log("Updated user input:", inputDetails.userInput);
  };

  useEffect(() => {
    const interestValue = inputDetails.userInput.interests; // updated key
    console.log("Loaded interest value:", interestValue);
    if (interestValue && interestValue !== "") {
      setAlreadyFilled(true);
      setInterest(interestValue);
      setActiveInterest(InterestArray.indexOf(interestValue));
    }
  }, [inputDetails.userInput.interests]);

  return (
    <div className="w-full px-4 flex flex-col justify-between h-full">
      <h1 className="w-full py-4 heading-style text-white">
        Pick Recipient's Interests
      </h1>

      <div className="w-full py-4 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {InterestArray.length ? (
          InterestArray.map((interest, index) => (
            <InterestCard
              key={index}
              setInterest={setSelectedInterest}
              setActiveInterest={setActiveInterest}
              active={activeInterest === index}
              interest={interest}
              index={index}
              selectedInterest={selectedInterest}
            />
          ))
        ) : (
          <div className="w-full text-center font-semibold p-4 text-xl">
            Interests were not found
          </div>
        )}
      </div>

      <PrevNext input={selectedInterest} alreadyFilled={alreadyFilled} />
    </div>
  );
};

export default InterestInputStep;
