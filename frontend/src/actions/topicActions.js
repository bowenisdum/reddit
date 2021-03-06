export const FETCH_TOPICS = 'FETCH_TOPICS';
export const RECEIVE_TOPICS = 'RECEIVE_TOPICS';

export function receiveTopics(json) {
  return { type: RECEIVE_TOPICS, topics: json };
}

export function fetchTopics() {
  const topics = [
    { title: 'Topic 1', votes: 20, commentCount: 5000 },
    { title: 'Topic 2', votes: 100, commentCount: 100 },
  ];

  return (dispatch) => {
    console.log(topics);
    return dispatch(receiveTopics(topics));
  };
}
