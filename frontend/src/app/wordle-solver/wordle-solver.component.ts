import { Component, ElementRef, EventEmitter, Output, QueryList, ViewChildren } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { WordleService } from './wordle.service';


@Component({
  selector: 'app-wordle-solver',
  standalone: true,
  imports: [],
  templateUrl: './wordle-solver.component.html',
  styleUrl: './wordle-solver.component.css'
})
export class WordleSolverComponent {


  @ViewChildren('box') boxElements!: QueryList<ElementRef>;
  @Output() colorSubmit = new EventEmitter<number[]>();

  boxContainer = document.getElementById('boxContainer');
  submitButton = document.getElementById('submitButton');

  letters = ['A', 'B', 'C', 'D', 'E'];
  colors = ['white', 'yellow', 'green'];
  colorValues: { [key: string]: number } = {
    'white': 0,
    'yellow': 1,
    'green': 2
  };
  
  constructor(
    public wordleService: WordleService,
    public route: Router
  ){}

  createBoxes() {
    this.letters.forEach(letter => {
        const box = document.createElement('div');
        box.className = 'box white';
        box.textContent = letter;
        box.addEventListener('click', () => this.changeColor(box));
        this.boxContainer?.appendChild(box);
    });
  }

  changeColor(box: { className: string; }) {
    const currentColor = box.className.split(' ')[1];
    const nextColorIndex = (this.colors.indexOf(currentColor) + 1) % this.colors.length;
    box.className = `box ${this.colors[nextColorIndex]}`;
  }

  // submitColors() {
  //   const colorData = Array.from(this.boxContainer?.children).map(box => {
  //     const color = box.className.split(' ')[1];
  //     return this.colorValues[color];
  //   });
  //   console.log('Color data:', colorData);
  //   // Here you would send the colorData to your Angular component
  //   // For example: sendToAngularComponent(colorData);
  // }

}
