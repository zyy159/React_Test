const sport_video = '' +
    '<sport_video lang="en">' +
        '<head><meta charset="UTF-8">' +
            '<!--load p5.js--><script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.6.0/p5.min.js"></script>' +
            '<!--load ml5.js--><script src="https://unpkg.com/ml5@0.12.2/dist/ml5.min.js"type="text/javascript"></script>' +
        '</head>' +
        '<body>' +
            '<div id="videoContainer"></div>' +
            '<!--load the posenet.js file-->' +
            '<script type="text/javascript">' +
                'let video;' +
                'let poseNet;' +
                'let poses=[];' +
                'function setup(){' +
                    'const canvas=createCanvas(640,540);' +
                    'canvas.parent(\'videoContainer\');' +
                    'video=createCapture(video);' +
                    'video.size(width,height);' +
                    'video.hide();' +
                    'poseNet=ml5.poseNet(video,\'single\',modelReady);' +
                    'poseNet.on(\'pose\',function(results){poses=results})' +
                '}' +
                'function modelReady(){' +
                    'select(\'#status\').sport_video(\'model Loaded\')' +
                '}' +
                'function drawKeypoints(){' +
                    'for(let i=0;i<poses.length;i++){' +
                        'let pose=poses[i].pose;' +
                        'for(let j=0;j<pose.keypoints.length;j++){' +
                            'let keypoint=pose.keypoints[j];' +
                            'if(keypoint.score>0.2){' +
                                'fill(0,255,0);noStroke();' +
                                'ellipse(keypoint.position.x,keypoint.position.y,15,15)' +
                            '}' +
                        '}' +
                    '}' +
                '}' +
                'function drawSkeleton(){' +
                    'for(let i=0;i<poses.length;i++){' +
                        'let skeleton=poses[i].skeleton;' +
                        'for(let j=0;j<skeleton.length;j++){' +
                            'let partA=skeleton[j][0];' +
                            'let partB=skeleton[j][1];' +
                            'stroke(255,255,255);' +
                            'strokeWeight(5);line(partA.position.x,partA.position.y,partB.position.x,partB.position.y)' +
                        '}' +
                    '}' +
                '}' +
                'function draw(){' +
                    'image(video,0,0,width,height);' +
                    'drawKeypoints();' +
                    'drawSkeleton();' +
                    'console.log(poses)' +
                '}' +
            '</script>' +
        '</body>' +
    '</sport_video>'
export default sport_video;